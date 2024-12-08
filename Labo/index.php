<?php 
    
    echo 1 + "1";  // 2 (INTEGER)
    echo "<br/><br/>";  
    echo "1" + "1";  // 2 (INTEGER)
    echo "<br/><br/>";
    echo 1 + 1;  // 2 (INTEGER)
    echo "<br/><br/>";
    echo "1 + 1 = 2"; //  1 + 1 = 2 (STRING)
    echo "<br/><br/>";
    echo 2 * "2";  // 4 (INTEGER)
    echo "<br/><br/>";
    echo "2" * "2";  // 4 (INTEGER)
    echo "<br/><br/>";
    echo 2 / 2;  // 1 (INTEGER)
    echo "<br/><br/>";
    echo 2 - 2;  // 0 (INTEGER)
    echo "<br/><br/>";
    echo True + true;  // 2 (INTEGER)
    echo "<br/><br/>";

    echo 1 + "5 Number"; // Error 6
    echo "<br/><br/>";
    echo 2 + (bool) "true";  //  3 (INTEGER)
    echo "<br/><br/>";
    echo 1 + (int) "100 hi";  // 101 (INTEGER)  
    echo 1 + (integer) "hi 100";  // 1  (INTEGER)
    