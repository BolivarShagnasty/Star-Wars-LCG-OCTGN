    # Python Scripts for the Star Wards LCG definition for OCTGN
    # Copyright (C) 2012  Konstantine Thoukydides

    # This python script is free software: you can redistribute it and/or modify
    # it under the terms of the GNU General Public License as published by
    # the Free Software Foundation, either version 3 of the License, or
    # (at your option) any later version.

    # This program is distributed in the hope that it will be useful,
    # but WITHOUT ANY WARRANTY; without even the implied warranty of
    # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    # GNU General Public License for more details.

    # You should have received a copy of the GNU General Public License
    # along with this script.  If not, see <http://www.gnu.org/licenses/>.

    
Resource = ("Resource", "62a2ba76-9872-481b-b8fc-ec35447ca640") #Temp 
Damage = ("Damage", "38d55f36-04d7-4cf9-a496-06cb84de567d") # Temp
Shield = ("Shield", "e9a419ff-5154-41cf-b84f-95149cc19a2a") # Temp

    
mdict = dict( # A dictionary which holds all the hard coded markers (in the markers file)
             Focus =                   ("Resource", "c93d4582-16a0-4e2d-9e63-71be20fbfa0c"),
             Damage =                  ("Damage", "224b865d-173b-49fd-9aed-17df678259b0"),
             Shield =                  ("Shield", "8559643f-7a15-4605-937d-0f39d59c9eda"),
             PlusOnePerm =             ("Permanent +1", "2246648d-1581-4be9-9636-1b75129313a6"),
             PlusOne =                 ("Temporary +1", "987d0d3f-0965-49ae-a96c-03394783d47a"),
             MinusOne =                ("Temporary -1", "21487438-e108-4f0c-a804-bd2a7f9a1ae5"),
             Edge =                    ("The Edge", "6ca2a796-1023-4ccf-9946-2fe4d2252c0c"))

resdict = {
             'Resource:Sith' :                 ("Sith Resource", "960e830a-fc0c-46ed-89be-6ac8efb5da8b"),
             'Resource:Imperial Navy' :        ("Imperial Navy Resource", "28fc888e-527e-453e-b9ba-263d36ea94dd"),
             'Resource:Scum and Villainy' :    ("Scum & Villainy Resource", "5b96ecac-4570-43f3-81bd-c81be0b4b602"),
             'Resource:Rebel Alliance' :       ("Rebel Alliance Resource", "cd947edc-ae8b-4983-822a-88f8dc6a86f2"),
             'Resource:Jedi' :                 ("Jedi Resource", "ee546e3c-de9c-43d1-9ad4-943645644c72"),
             'Resource:Smugglers and Spies' :  ("Smugglers & Spies Resource", "bc58905b-1f57-4297-9199-837c85a8ef0d"),
             'Resource:Neutral' :              ("Neutral", "fae80b84-88f5-46fe-9806-ed624265757f")}



UnpaidColor = "#ffd700"
SelectColor = "#009900"
LightForceColor = "#ffffff"
DarkForceColor = "#000000"
CapturedColor = "#888888" # Cards which are in play but captured by the dark side
AttackColor = "#ff0000"
DefendColor = "#0000ff"
EdgeColor = "#c0c0c0"
FateColor = "#ae39d4"

Xaxis = 'x'
Yaxis = 'y'

phases = [
    "Opponent's Turn",
    "=== Balance Phase: {} ===".format(me),
    "=== Refresh Phase: {} ===".format(me),
    "=== Draw Phase: {} ===".format(me),
    "=== Deployment Phase: {} ===".format(me),
    "=== Conflict Phase: {} ===".format(me),
    "=== Force Phase: {} ===".format(me)]

engagementPhases = [
    "+++ Engagement: Declare Objective +++",
    "+++ Engagement: Declare Attackers +++",
    "+++ Engagement: Declare Defenders +++",
    "+++ Engagement: Edge Battle: +++",
    "+++ Engagement: Resolve Strikes +++",
    "+++ Engagement: Reward Unopposed +++"]
    