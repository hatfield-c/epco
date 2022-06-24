using UnityEngine;
using UnityEditor;

[CustomEditor(typeof(SceneManager))]
public class EditorTrainGenerator : Editor
{
    public override void OnInspectorGUI() {
        base.OnInspectorGUI();

        SceneManager manager = (SceneManager)this.target;

        EditorGUILayout.LabelField("Active Inference", EditorStyles.boldLabel);

        if (GUILayout.Button("Enter Active Inference Mode")) {
            manager.ActiveInference();
        }

        EditorGUILayout.LabelField("Constraints", EditorStyles.boldLabel);

        if (GUILayout.Button("Render Constraint Space")) {
            manager.RenderConstraintSpace();
        }

        EditorGUILayout.LabelField("Training", EditorStyles.boldLabel);

        if (GUILayout.Button("Generate Training Data")) {
            manager.GenerateTrainingData();
        }
    }
}
