using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class StreamManager : MonoBehaviour
{
    [SerializeField]
    protected List<GameObject> sourceObjects = new List<GameObject>();

    protected List<string> sourceIds = new List<string>();
    protected Dictionary<string, DataStreamInterface> sources = new Dictionary<string, DataStreamInterface>();

    void Start()
    {
        DataStreamInterface source;
        string sourceId;
        
        for(int i = 0; i < this.sourceObjects.Count; i++) {
            source = this.sourceObjects[i].GetComponent<DataStreamInterface>();
            sourceId = source.GetId();

            this.sourceIds.Add(sourceId);
            this.sources.Add(sourceId, source);
        }
    }

    void FixedUpdate()
    {
        string sourceId;
        float[] data;

        for(int i = 0; i < this.sources.Count; i++) {
            sourceId = this.sourceIds[i];
            data = this.sources[sourceId].GetData(Time.fixedTime);

            string output = $"{Time.fixedTime} Source {i} ({sourceId}) :";

            for(int j = 0; j < data.Length; j++) {
                output += $" {data[j]},";
            }

            //Debug.Log(output);
        }
    }

    public List<string> GetSourceIds() {
        return this.sourceIds;
    }

    public Dictionary<string, DataStreamInterface> GetSources() {
        return this.sources;
    }

    public int GetStreamCount() {
        return this.sourceIds.Count;
    }
}
