public class Game
{
    public int ID;
    public List<List<Cube>>? Throws;

    public Game()
    {
        Throws = new List<List<Cube>>();
    }

    public bool IsGamePossible(IDictionary<string, int> config)
    {
        if (Throws == null) Throws = new List<List<Cube>>();

        foreach (var aThrow in Throws)
        {
            foreach (var cubeSet in aThrow)
            {
                string colorName = cubeSet.Name ?? "";
                if (cubeSet.Count > config[colorName])
                {
                    return false;
                }
            }
        }

        return true;
    }

    public IDictionary<string, int> GetFewest()
    {
        IDictionary<string, int> fewestNeeded = new Dictionary<string, int>();

        foreach (var aThrow in Throws)
        {
            foreach (var cube in aThrow)
            {
                if (!fewestNeeded.ContainsKey(cube.Name)) fewestNeeded.Add(cube.Name, cube.Count);
                if (fewestNeeded[cube.Name] < cube.Count) fewestNeeded[cube.Name] = cube.Count;
            }
        }

        return fewestNeeded;
    }
}