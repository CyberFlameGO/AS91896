# AS91896 Develop a computer program (2.7 Digital Technologies)
Current idea: make a wordle-type game which stores to a database on each attempt, so a user can potentially visualise all their attempts. Also make Wordle letters variable and guess amounts variable potentially

Addressable caveats: 
* Window closing without game ending (by either winning or running out of guesses)
    * Addressable by auto-saving to SQLite every 15-30 seconds, and storing a boolean value stating if the "run" is complete or not (we won't auto-update on every word guess)
  

