# Baseball Head-to-Head Records Table

## Solution Explanation

This program reads team head-to-head records from a JSON file and displays wins in a head-to-head table format.

### Approach
1. Load the JSON data containing each team's records against opponents
2. Extract all team names and store them in a sorted list
3. Use nested loops to build a 2D array:
   - Outer loop iterates through each team (rows)
   - Inner loop iterates through opponents (columns)
   - When team == opponent, store "--" (teams don't play themselves)
   - Otherwise, store the win count from the JSON data
4. Print the matrix with formatted columns

### Data Structure
The input JSON is structured as:
```
{
  "TEAM": {
    "OPPONENT": { "W": <wins>, "L": <losses> }
  }
}
```
### Example Output
```
| Tm|BRO|BSN|CHC|CIN|NYG|PHI|PIT|STL|
|BRO| --| 10| 15| 15| 14| 14| 15| 11|
|BSN| 12| --| 13| 13| 13| 14| 12|  9|
|CHC|  7|  9| --| 12|  7| 16|  8| 10|
|CIN|  7|  9| 10| --| 13| 13| 13|  8|
|NYG|  8|  9| 15|  9| --| 12| 15| 13|
|PHI|  8|  8|  6|  9| 10| --| 13|  8|
|PIT|  7| 10| 14|  9|  7|  9| --|  6|
|STL| 11| 13| 12| 14|  9| 14| 16| --|
```