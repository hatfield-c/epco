using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class SceneManager : MonoBehaviour
{
    [SerializeField]
    protected StreamManager streamManager = null;

    [SerializeField]
    protected ConstraintManager constraintManager = null;

    [SerializeField]
    protected TrainGenerator trainGenerator = null;

    public void GenerateTrainingData() {
        this.trainGenerator.GenerateData();
    }
}
