# AS91896 Develop a computer program (2.7 Digital Technologies)
Current idea: make an endless climber game which stores to a database on each attempt, so a user can potentially visualise all their attempts

Addressable caveats: 
* Window closing without game ending (by death)
    * Addressable by auto-saving to SQLite every 15-30 seconds, and storing a boolean value stating if the "run" is complete or not (we won't auto-update on every climb)
    
I want to also use programmer art, and instead of randomizing the position of every climbable platform, just detect for when the player reaches a certain stage and make things more difficult on the code end (potentially moving the platforms)

