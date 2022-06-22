using System.Collections;
using System.Collections.Generic;
using UnityEngine;

using System;
using System.Net;
using System.Net.Sockets;
using System.Text;

public class EpcManager : MonoBehaviour
{

    protected TcpClient socketConnection = null;
    protected NetworkStream networkStream = null;

    void Start()
    {
        byte[] bytes = new byte[1024];

        Debug.Log("Sending data");

        System.Diagnostics.Stopwatch connectionTimer = new System.Diagnostics.Stopwatch();
        connectionTimer.Start();

        bool attemptConnection = true;
        while (attemptConnection) {

            if (connectionTimer.ElapsedMilliseconds / 1000 < 30) {
                this.socketConnection = new TcpClient();
                this.socketConnection.Connect("localhost", 7777);
                this.networkStream = this.socketConnection.GetStream();

                attemptConnection = false;
            } else {
                connectionTimer.Stop();
                UnityEngine.Debug.LogError("Connection timed out before an attempted connection was made by the server.");

                return;
            }
        }

        connectionTimer.Stop();

        if (this.socketConnection == null) {
            UnityEngine.Debug.LogError("No server connection was found. SendMessage() aborted.");
        }

        try {
            if (this.networkStream.CanWrite) {
                byte[] encodedMessage = Encoding.ASCII.GetBytes("Connection success!");

                this.networkStream.Write(encodedMessage, 0, encodedMessage.Length);
            }
        } catch (System.Exception exception) {
            UnityEngine.Debug.Log(exception.StackTrace);
            UnityEngine.Debug.Log(exception.Message);
            UnityEngine.Debug.LogError("Exception thrown while trying to send message to SUMO. Discarding message.");
        }

    }

}
