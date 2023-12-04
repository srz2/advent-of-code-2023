using System.IO;
using System.Linq;

// Get data
const string inputFile = "../data/sample1.dat";
if (!File.Exists(inputFile)) {System.Console.WriteLine("Input file not found"); Environment.Exit(1);}
string[] lines = File.ReadAllLines(inputFile);
// System.Console.WriteLine(string.Join(Environment.NewLine, lines));

// Get Config
var configLine = lines[0];
if (!configLine.StartsWith("Bag")) throw new Exception("Missing custom line for configuration");
// Assuming my config of bag is the only bag configured
var config = new Dictionary<string, int>();
var configCubes = configLine.Substring(configLine.IndexOf(":") + 1).Trim().Split(",");
foreach (var set in configCubes)
{
    var parts = set.Trim().Split(" ");
    config.Add(parts[1], Convert.ToInt32(parts[0]));
}

// Parse Games
var games = new List<Game>();
for (int c = 1; c < lines.Length; c++)
{
    // System.Console.WriteLine($"GAME {lines[c]}");
    var pos = lines[c].IndexOf(":");
    var gameInfo = lines[c].Substring(0, pos).Split().Select(x => x.Replace(":", "").Trim()).ToList();

    // Get info
    var type = gameInfo[0];
    var id = Convert.ToInt32(gameInfo[1]);
    if (type != "Game") {throw new Exception("Unexpected game type");}
    Game newGame = new Game
    {
        ID = id,
    };

    // Parse game throw
    var gameThrows = lines[c].Substring(pos + 1).Split(";", StringSplitOptions.RemoveEmptyEntries).Select(x => x.Trim());
    // System.Console.WriteLine($"ALL GAME THROWS: {string.Join(",", gameThrows)}");
    foreach (string gameThrow in gameThrows)
    {
        newGame.Throws?.Add(new List<Cube>());

        var singleThrow = gameThrow.Split(",").Select(x => x.Trim()).ToList();
        // System.Console.WriteLine($"SINGLE THROW: {string.Join("|", singleThrow)}");
        foreach (string rawCube in singleThrow)
        {
            var parts = rawCube.Split(" ", StringSplitOptions.None);
            newGame.Throws?.Last().Add(new Cube{
                Count = Convert.ToInt32(parts[0]),
                Name = parts[1]
            });
        }
    }

    games.Add(newGame);
}

var value = 0;
foreach (var game in games)
{
    bool isPossible = game.IsGamePossible(config);
    value += isPossible ? game.ID : 0;
}
System.Console.WriteLine("Solution 1 Result: " + value);

value = 0;
foreach (var game in games)
{
    int power = 1;
    IDictionary<string, int> fewestInGame = game.GetFewest();
    foreach(var key in fewestInGame.Keys)
    {
        power *= fewestInGame[key];
    }

    value += power;
}
System.Console.WriteLine("Solution 2 Result: " + value);
