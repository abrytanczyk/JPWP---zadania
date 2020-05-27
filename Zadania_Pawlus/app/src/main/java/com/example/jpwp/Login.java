package com.example.jpwp;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.util.Base64;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class Login extends AppCompatActivity {
    Button buttonLogin;
    EditText textEmail, textPassword;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);

        buttonLogin=(Button)findViewById(R.id.btn_login2);
        textEmail=(EditText) findViewById(R.id.txt_loginEmail);
        textPassword=(EditText) findViewById(R.id.txt_loginPassword);

        //done - napisz obsługę przycisky buttonLogin, nie zapomnij o hashowaniu hasla
        buttonLogin.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String email=textEmail.getText().toString();
                String password = Base64.encodeToString(textPassword.getText().toString().getBytes(), Base64.DEFAULT);  //hashowanie hasła
                String type="login";
                BackgroundTask backgroundTask= new BackgroundTask(getApplicationContext());
                backgroundTask.execute(type, email, password);

            }
        });
    }
}
