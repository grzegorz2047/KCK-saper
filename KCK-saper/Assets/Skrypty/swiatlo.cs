using UnityEngine;
using System.Collections;

public class ExampleClass : MonoBehaviour {
    public Light lt;
    void Start() {
        lt = GetComponent<Light>();
    }
    void Update() {
        lt.color -= Color.white / 2.0F * Time.deltaTime;
    }
}