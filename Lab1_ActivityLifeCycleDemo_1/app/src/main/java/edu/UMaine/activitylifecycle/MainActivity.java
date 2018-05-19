package edu.UMaine.activitylifecycle;

import android.os.Bundle;
import android.app.Activity;
import android.content.Intent;
import android.view.Menu;
import android.view.View;
import android.widget.Toast;

public class MainActivity extends Activity {

	@Override
	public void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);
		Toast.makeText(this, "onCreate() ......", Toast.LENGTH_SHORT).show();
	}

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		getMenuInflater().inflate(R.menu.activity_main, menu);
		Toast.makeText(this, "onCreateOptionsMenu() ......", Toast.LENGTH_SHORT).show();
		return true;
	}

	public void onStart() {
		super.onStart();
		Toast.makeText(this, "onStart() ......", Toast.LENGTH_SHORT).show();
	}
	
	public void onRestart() {
		super.onStart();
		Toast.makeText(this, "onRestart() ......", Toast.LENGTH_SHORT).show();
	}

	public void onResume() {
		super.onResume();
		Toast.makeText(this, "onResume() ......", Toast.LENGTH_SHORT).show();
	}

	public void onPause() {
		super.onPause();
		Toast.makeText(this, "onPause() ......", Toast.LENGTH_SHORT).show();
	}

	public void onStop() {
		super.onStop();
		Toast.makeText(this, "onStop() ......", Toast.LENGTH_SHORT).show();
	}

	public void onDestroy() {
		super.onDestroy();
		Toast.makeText(this, "onDestroy() ......", Toast.LENGTH_SHORT).show();
	}
}
