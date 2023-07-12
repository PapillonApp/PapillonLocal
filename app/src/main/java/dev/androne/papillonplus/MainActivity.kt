package dev.androne.papillonplus

import android.content.*
import android.content.pm.PackageManager
import android.net.Uri
import android.os.Bundle
import android.widget.Toast
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.viewModels
import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.Composable
import androidx.compose.runtime.MutableState
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import androidx.lifecycle.LiveData
import androidx.lifecycle.ViewModel

import dev.androne.papillonplus.ui.theme.PapillonPlusTheme
import java.net.HttpURLConnection
import java.net.URL
import kotlinx.coroutines.*



class MainActivity : ComponentActivity() {
    class MainViewModel : ViewModel() {
        val isRunning = mutableStateOf(false)

        fun startServer() {
            isRunning.value = true
        }

        fun stopServer() {
            isRunning.value = false
        }

        // getter
        fun getIsRunning() : Boolean {
            return isRunning.value
        }
    }
    val viewModel: MainViewModel by viewModels()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            PapillonPlusTheme {
                // A surface container using the 'background' color from the theme
                Surface(modifier = Modifier.fillMaxSize(), color = MaterialTheme.colorScheme.background) {
                    Home(this, viewModel, ::openPapillonApp, getSystemService(Context.CLIPBOARD_SERVICE) as ClipboardManager)
                }
            }
        }
        val intent = Intent(this, HugServerService::class.java)
        startService(intent)

        GlobalScope.launch {
            openPapillonPlusWhenServerStarted()
        }

    }

    fun stopService() {
        val intent = Intent(this, HugServerService::class.java)
        stopService(intent)
        viewModel.stopServer()
    }




    fun openPapillonApp() {
        val intent = Intent().apply {
            component = ComponentName("plus.pronote.app", "plus.pronote.app.MainActivity")
            flags = Intent.FLAG_ACTIVITY_NEW_TASK
        }
        try {
            startActivity(intent)
        } catch (e: ActivityNotFoundException) {
            // L'application n'est pas installée. Vous pouvez ouvrir la page du Play Store de l'application ici
            val uri = Uri.parse("market://details?id=plus.pronote.app")
            val goToMarket = Intent(Intent.ACTION_VIEW, uri)
            startActivity(goToMarket)
        }
    }


    fun waitForServeurStarted() {
        // request to http://localhost:8000/info until it returns 200
        var isOk = false
        while (!isOk) {
            try {
                val url = URL("http://127.0.0.1:8000/infos")
                val con: HttpURLConnection = url.openConnection() as HttpURLConnection
                con.requestMethod = "GET"
                val responseCode = con.responseCode
                if (responseCode == HttpURLConnection.HTTP_OK) {
                    isOk = true
                    // server started
                    viewModel.startServer()

                }
            } catch (e: Exception) {
                // do nothing

            }
            Thread.sleep(100)
        }


    }

    fun openPapillonPlusWhenServerStarted() {
        waitForServeurStarted()
        openPapillonApp()
    }
}

@Composable
fun Home(context:Context, mainViewModel : MainActivity.MainViewModel, openPapillonApp: () -> Unit = {}, clipboardManager: ClipboardManager? = null) {
    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(16.dp),
        verticalArrangement = Arrangement.Center,
        horizontalAlignment = Alignment.CenterHorizontally
    ) {
        Text(text = "Papillon+")
        Spacer(modifier = Modifier.height(16.dp))
        if (mainViewModel.getIsRunning()) {
            Text(text = "Le serveur est lancé")
        } else {
            Text(text = "Le serveur est en cours de lancement")
            // loading indicator


        }
       Spacer(modifier = Modifier.height(16.dp))
        // open papillon app

        Button(onClick = {
            openPapillonApp()
        }, enabled = mainViewModel.getIsRunning()) {
            Text(text = "Ouvrir Papillon")
        }

        Spacer(modifier = Modifier.height(16.dp))
        Text(text = "N'oubliez pas de definir l'adresse du serveur dans les paramètres de l'application Papillon à l'adresse http://127.0.0.1:8000")
        Spacer(modifier = Modifier.height(8.dp))
        Button(onClick = {
            // copy server address
            if(clipboardManager != null) {
                val clip = ClipData.newPlainText("http://127.0.0.1:8000", "http://127.0.0.1:8000")
                clipboardManager.setPrimaryClip(clip)
                // show toast
                Toast.makeText(context,
                    "Adresse du serveur copiée dans le presse papier"
                    , Toast.LENGTH_SHORT).show()
            }

        }) {
            Text(text = "Copier l'adresse du serveur")
        }



    }
}

@Preview(showBackground = true)
@Composable
fun DefaultPreview() {
    PapillonPlusTheme {
        Home(context = MainActivity(), mainViewModel = MainActivity.MainViewModel())
    }
}