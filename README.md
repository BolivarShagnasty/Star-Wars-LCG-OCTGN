﻿Star Wars:The Card Game LCG plugin for OCTGN
=========================
The Star Wars universe as a Head2Head Living card game

Enjoy!

Tutorials
---------

[Step-by-Step Tutorial Video (v.1.0.2)](https://vimeo.com/54797455)

Screenshots
---------
(Click for larger size)

The Dark side destroys the last objective to win the game

[![](http://i.imgur.com/Ooq0Vl.png)](http://i.imgur.com/Ooq0V.png)

Demo game at v1.0.0

[![](http://i.imgur.com/GutHll.jpg)](http://i.imgur.com/GutHl.jpg)

Changelog
---------

### 1.1.3

* Refresh Phase should not clear opponent's shield tokens anymore.

### 1.1.2

* Fixed Rebel Sympathizer reducing costs for both sides without being used at all
* Fixed Red Two Automation

### 1.1.1

* Light Side now really shouldn't refresh on their first turn.
* Card placement on second row should now be fine.

### 1.1.0

* **Desolation of Hoth** cards have been added and scripted. Grab the latest pack for the goodies.
* General scripting improvements which should make future sets easier to script
* Now cards which reduce/incease card costs will be checked when a card is first attempted to be played. 


### 1.0.17

* Zoomed in on the table so that the cards are better seen without having to mouse over them. Re-arranged the placement to make this possible.
* Recon Mission will now reduce the dark-side's reserves when it leaves play, and not the light side's
* You can now cancel a card ability that you've triggered. You can find the appropriate function on the "Manual Actions" menui
* You can now force a card ability (for example if you reduced the cost) . Just double click the card and it will ask you if you want to bypass the payment
* Disturbance in the Force now only target opponent's units
* Added a new message at the end of the game to inform people where to report bugs

### 1.0.16

* Fixed Darth Vader's ability triggering but doing nothing
* Fixed Superlaser Blast not increasing the Death Star Dial
* Fixed Endor Gambit removing focus from opposing units when only those are there.
* Turns sequence will now use the OCTGN internal method to change player, which should look nicer
* Made the hand size icon fit better in the new theme.

### 1.0.15

* Robustness fixes
* Fixed Take Them Prisoner Bug

### 1.0.14

* Game will now check player decks during setup for legality
* A Change in the way events work. Now as soon as you finish paying the cost for an event, the card will change its highlight to green to signify the event is ready to take effect. It is at this point that your opponent is allowed to play interrupts.
  * Interrupts which cancel the effects of events, like C-3PO new require a "ready" event as a target. A "ready event" is an event with a green highlight which has been paid for (or has 0 cost). When that happens, the event will not have any effects when activated by your opponent.
  * Once all players had a chance to play interrupts to events, the controller of each ready event can now double-click on it to have it take effect
  

### 1.0.13

* Common Ground works automatically now
* Recon Mission now reduces its owner's reserves when discarded, and not the rebels'

### 1.0.12

* Reorganized menus
* Added ability to rescue targets
* Leia's ability should not trigger twice
* Fixed Placement of captured and attached cards by opponent's scripts
* Stolen Plans should now work automatically

### 1.0.11

Important bugfixes for the automations

* Now scripts on cards triggered by another player's effects should work
* Leia's Ability should now be working
* Rebel Sympathizer's ability is automated
* Trooper Assault should work now.
* Conceding the game shouldn't give an error anymore
* Various robustness changes.

### 1.0.10

Card automations are now here! 
A very large percentage of the available cards will now trigger their effects as soon as they hit the table 
or as soon their triggers are reached (after specific phases, after striking etc). 
Cards which have their own abilities are also automated, and you can make them work by simply double-clicking on them and having the target of their effect targeted (if one is needed)

So except that, the following have also been done:

* Added capturing mechanic. Many automations will use it automatically, but you can also call it manually.
  * To capture a card from the table, opponents hand or opponent's deck simply target their card and press Ctrl+C on the table. Yes you can target a card in a player's hand or deck normally (shift+click)
* Added a rescuing mechanic. When an objective with captured cards is destroyed, captured cards in it will be returned to their owner's hands. 
  * If you want to manually rescue cards, the controller of the card needs to simply use the "Manual Actions > Rescue card" option
  * IMPORTANT: Due to the attachment mechanics of capturing cards, **You should not move them away from their objective manually**. Use the rescue mechanic
  * If for some reason the rescue mechanic does not work or cannot be used, and you want to clear the cards that are supposedly captured in an objective, use the "Clear of captured variables" option under "Manual Actions".  
* During setup, starting objectives are now placed face down. This allows players to perform their mulligans before using the abilities of those objectives  
  * Once both players have setup their three starting objectives, they just need to double-click on them to reveal them.
* Smugglers & Scouts resources should now be counted correctly.
* Unopposed Bonus is now only applied if the attacker has units left in battle
* Mulligan will now only ever provide 6 cards


### 1.0.4 

* Fixed bug where finishing an unopposed engagement would assign 2 damage
* Thwarting an objective will now ask for confirmation to avoid mistakes
* Renamed the card discard function to point out that it also thwarts objectives.
* Balance of the Force will now spawn on the light side to avoid confusion

### 1.0.3

New version improves engagement by separating it into steps (i.e. phases) as well. 
This means that you can easily communicate who's turn it is to declare participants or when you're ready to start playing edge cards and so on.

The steps work as always, once you're in an engagement, simple press Ctrl+Enter to move to the next step.
The game is also smart enough to auto-announce a phase when you take an action that belongs to it
(For example if you play an edge card, the game will announce the "Edge Battle" step). 

This also includes some extra automation to make things faster and more robust. Reaching the "Reward Unopposed" step will automatically end the engagement, and reaching the strikes step will make sure the edge battle is resolved.

* Fixed various bugs during Edge calculations, such as cards not being revealed
* Now unopposed attacker wins the edge struggle automatically
* Fate cards now have a different highlight when revealed. Once they've been used, they switch to the normal silver highlight for the calculation
* You can now clear participants form the battle or remove units from the force. Normally the game does not allow you, but this is in case you've done a mistake
* Added an option to grab the Edge manually, if for some reason the edge calculation was incorrect

### 1.0.1

* Finishing the engagement now clears the opponent's edge cards as well
* Tactic:1 strikes now focus the target unit
* Spread out the objectives a bit
* Free units/enhancements now are autoplaced.
* Can now manually shuffle the objective deck

### 1.0.0

First working version for the public. It has basic gameplay functionality but not card scripting (i.e. individual card effects are not automated)

However the basic things you need to do quickly and effortlessly should be possible. 

http://i.imgur.com/GutHl.jpg