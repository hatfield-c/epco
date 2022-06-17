using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public interface DataStreamInterface {
    string GetStreamType();
    string GetId();
    float[] GetData(float currentTime);
    void SetData(float[] data);
    List<List<float>> GetBounds();
    int GetSize();
}
