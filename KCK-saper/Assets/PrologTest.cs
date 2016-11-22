using UnityEngine;
using System.Collections;
using System;
using System.Diagnostics;
using System.IO;

public class PrologTest : MonoBehaviour {

	// Use this for initialization
	void Start () {
		String path = System.Reflection.Assembly.GetExecutingAssembly().Location;
		string[] folders = path.Split('\\');
		String newPath = "";
		for (int i = 0; i < folders.Length-1; i++)
		{
			newPath += folders[i] + "\\";
		}
		UnityEngine.Debug.Log("out: " + newPath);
		String pyscript = "example.py";
		UnityEngine.Debug.Log(path);
		run_cmd("\""+newPath+pyscript+"\"", "");
        //run_cmd("print", "\"hello world\"");

    }
	
	// Update is called once per frame
	void Update () {
	
	}
    private void run_cmd(string cmd, string args)
    {
        ProcessStartInfo start = new ProcessStartInfo();
        start.FileName = "C:\\Python27\\python.exe";
        start.Arguments = string.Format("{0} {1}", cmd, args);
        start.UseShellExecute = false;
        start.RedirectStandardOutput = true;
        using (Process process = Process.Start(start))
        {
            using (StreamReader reader = process.StandardOutput)
            {
                string result = reader.ReadToEnd();
                UnityEngine.Debug.Log("Wynik to " + result);
            }
        }
    }
}
