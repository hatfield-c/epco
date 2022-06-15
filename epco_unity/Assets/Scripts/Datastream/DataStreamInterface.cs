using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public interface DataStreamInterface {
    string GetStreamType();
    string GetId();
    float[] GetData(float currentTime);
    List<float> GetUpperBounds();
    List<float> GetLowerBounds();
    int GetSize();
}
