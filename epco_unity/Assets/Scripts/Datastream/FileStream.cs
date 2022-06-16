using System.Collections;
using System.Collections.Generic;
using System.IO;
using System;
using UnityEngine;

public class FileStream : MonoBehaviour, DataStreamInterface {
    [SerializeField]
    protected string streamId = "unnamed_filestream";

    [SerializeField]
    protected string filePath = null;

    [SerializeField]
    protected int eventSize = 0;

    [SerializeField]
    protected List<float> upperBounds = null;

    [SerializeField]
    protected List<float> lowerBounds = null;

    protected StreamReader reader = null;
    protected int eventCount = 0;
    protected int reportedSize = 0;
    
    protected float currentTime = 0;
    protected float[] currentData = null;

    protected float nextTime = 0;
    protected float[] nextData = null;

    void Start() {
        this.reader = new StreamReader("Assets/" + this.filePath);

        string line = this.reader.ReadLine();
        string[] data = line.Split(',');
        this.eventCount = Int32.Parse(data[0]);
        this.reportedSize = Int32.Parse(data[1]);

        if (this.eventSize != this.reportedSize) {
            Debug.LogError("Given event size does not match reported event size in file. Defaulting to given size.");
        }

        this.currentData = new float[this.eventSize];
        this.nextData = new float[this.eventSize];
    }

    public (List<float>, List<float>) GetBounds() {
        return (this.lowerBounds, this.upperBounds);
    }

    public float[] GetData(float currentTime) {

        while (currentTime >= this.nextTime) { 

            string line = this.reader.ReadLine();
            
            if (line == null) {
                break;
            }

            string[] data = line.Split(':');

            this.currentTime = this.nextTime;
            this.currentData = this.nextData;

            this.nextTime = float.Parse(data[0]);
            this.nextData = this.parseEventData(data[1]);
        }

        return this.currentData;
    }

    public void SetData(float[] data) {
        this.currentData = data;
    }

    public int GetSize() {
        return this.eventSize;
    }

    public string GetId() {
        return this.streamId;
    }

    public string GetStreamType() {
        return "filestream";
    }

    protected float[] parseEventData(string raw) {
        float[] parsed = new float[this.eventSize];
        string[] data = raw.Split(',');

        for(int i = 0; i < this.eventSize; i++) {
            parsed[i] = float.Parse(data[i]);
        }

        return parsed;
    }
}
