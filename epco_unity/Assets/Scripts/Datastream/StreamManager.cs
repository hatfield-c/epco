using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class StreamManager : MonoBehaviour
{
    [SerializeField]
    protected List<GameObject> sourceObjects = new List<GameObject>();

    protected List<DataStreamInterface> sources = new List<DataStreamInterface>();

    void Start()
    {
        for(int i = 0; i < this.sourceObjects.Count; i++) {
            DataStreamInterface source = this.sourceObjects[i].GetComponent<DataStreamInterface>();

            this.sources.Add(source);
        }
    }

    void FixedUpdate()
    {
        for(int i = 0; i < this.sources.Count; i++) {
            float[] data = this.sources[i].GetData(Time.fixedTime);

            string output = $"{Time.fixedTime} Source {i} ({this.sources[i].GetId()}) :";

            for(int j = 0; j < data.Length; j++) {
                output += $" {data[j]},";
            }

            Debug.Log(output);
        }
    }
}
