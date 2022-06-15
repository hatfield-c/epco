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

        List<float[]> bounds = this.CompileBounds();

        for (int i = 0; i < this.samples; i++) {
            float[] sample = this.GenerateSample(bounds);
            string encoded = this.EncodeSample(sample);

            if (this.constraintManager.IsValid(sample)) {
                encoded += ",1";
            } else {
                encoded += ",0";
            }
            //Debug.Log(encoded);
            writer.WriteLine(encoded);
        }

        writer.Close();
    }

    protected float[] GenerateSample(List<float[]> bounds) {
        int featureSize = bounds.Count;

        float[] sample = new float[featureSize];

        for(int i = 0; i < featureSize; i++) {
            sample[i] = UnityEngine.Random.Range(bounds[i][0], bounds[i][1]);
        }

        return sample;
    }

    protected string EncodeSample(float[] sample) {
        string encoded = "";

        for (int i = 0; i < sample.Length; i++) {
            encoded += sample[i].ToString();

            if(i < sample.Length - 1) {
                encoded += ",";
            }
        }

        return encoded;
    }

    protected List<float[]> CompileBounds() {
        List<float[]> allBounds = new List<float[]>();

        List<string> sourceIds = this.streamManager.GetSourceIds();
        Dictionary<string, DataStreamInterface> sources = this.streamManager.GetSources();
        
        for(int i = 0; i < this.streamManager.GetStreamCount(); i++) {
            string sourceId = sourceIds[i];

            List<float> upperBounds = sources[sourceId].GetUpperBounds();
            List<float> lowerBounds = sources[sourceId].GetLowerBounds();

            for(int j = 0; j < upperBounds.Count; j++) {
                float[] bounds = new float[2];
                bounds[0] = lowerBounds[j];
                bounds[1] = upperBounds[j];

                allBounds.Add(bounds);
            }
        }

        return allBounds;
    }
}
