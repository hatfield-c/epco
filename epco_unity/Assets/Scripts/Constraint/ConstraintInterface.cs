using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public interface ConstraintInterface
{
    bool IsValid(Dictionary<string, DataStreamInterface> sources);
}
