using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class FunctionStream : MonoBehaviour, DataStreamInterface {
    [SerializeField]
    protected int outSize = 1;
    
    [SerializeField]
    protected float scaleHeight = 1;
    protected float scaleWidth = 1;

    void Start() {
        
    }

    public float[] GetData(float currentTime) {
        float[] data = new float[this.outSize];

        for(int i = 0; i < data.Length; i++) {
            data[i] = Mathf.Sin(currentTime * this.scaleWidth) * this.scaleHeight;
        }

        return data;
    }

    public string GetId() {
        return "function";
    }
}
