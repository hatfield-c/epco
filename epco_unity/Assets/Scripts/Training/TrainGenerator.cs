using System;
using System.IO;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class TrainGenerator : MonoBehaviour
{
    [SerializeField]
    protected StreamManager streamManager = null;

    [SerializeField]
    protected ConstraintManager constraintManager = null;

    [SerializeField]
    protected int samples = 0;

    [SerializeField]
    protected string filePath = null;

    public void GenerateData()
    {
        if (!Application.isPlaying) {
            Debug.LogError("Error: You must be in Play mode to generate training data.");
            return;
        }

        string path = "Assets/" + filePath;
        StreamWriter writer = new StreamWriter(path);

        
        Dictionary<string, float[]> sample;

        for (int i = 0; i < this.samples; i++) {
            
            sample = this.GenerateSample();
            this.ApplySample(sample);

            string encoded = this.EncodeSample(sample);

            if (
                this.constraintManager.IsValid(this.streamManager.GetSources())
            ) {
                encoded += ",1";
            } else {
                encoded += ",0";
            }
            //Debug.Log(encoded);
            writer.WriteLine(encoded);
        }

        writer.Close();
    }

    protected void ApplySample(Dictionary<string, float[]> sample) {
        List<string> sourceIds = this.streamManager.GetSourceIds();
        Dictionary<string, DataStreamInterface> sources = this.streamManager.GetSources();

        for (int i = 0; i < sourceIds.Count; i++) {
            string sourceId = sourceIds[i];
            DataStreamInterface source = sources[sourceId];
            float[] data = sample[sourceId];

            source.SetData(data);
        }
    }

    protected Dictionary<string, float[]> GenerateSample() {
        Dictionary<string, (List<float>, List<float>)> bounds = this.streamManager.GetBounds();
        List<string> sourceIds = this.streamManager.GetSourceIds();

        Dictionary<string, float[]> sample = new Dictionary<string, float[]>();

        for (int i = 0; i < sourceIds.Count; i++) {
            string sourceId = sourceIds[i];
            (List<float> lowerBounds, List<float> upperBounds) = bounds[sourceId];

            float[] data = new float[lowerBounds.Count];
            for(int j = 0; j < lowerBounds.Count; j++) {
                data[i] = UnityEngine.Random.Range(lowerBounds[i], upperBounds[i]);
            }

            sample[sourceId] = data;
        }

        return sample;
    }

    protected string EncodeSample(Dictionary<string, float[]> sample) {
        List<string> sourceIds = this.streamManager.GetSourceIds();

        string encoded = "";

        for (int i = 0; i < sourceIds.Count; i++) {
            string sourceId = sourceIds[i];
            float[] data = sample[sourceId];

            for(int j = 0; j < data.Length; j++) {
                encoded += data[j].ToString();

                if (i < sourceIds.Count - 1 || j < data.Length - 1) {
                    encoded += ",";
                }
            }
        }

        return encoded;
    }
}
