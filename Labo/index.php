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
    echo 1 + 1.5;
    echo "<br/><br/>"; 
    echo gettype(10 + (int) "hi 100"); //  1  (INTEGER)
    echo "<br/>";
    echo 1 + (int) "hi 100";
    echo "<br/>";
    echo gettype(1 + 1.5);  //  2.5 (DOUBLE)
    echo "<br/>";    
    echo gettype(1 + (int) 1.5);  // 2.5  (INTEGER)

    
    var_dump((bool)"");   //  bool(false)
    var_dump((bool) "0");   // bool(false)
    var_dump((bool) "1"); // bool(true)
    var_dump((bool)"hi"); // bool(true)
    var_dump((bool) []);  // bool(false)
    var_dump((bool) [1]); // bool(true)
    var_dump((bool) [2,3]); // bool(true)
    var_dump((bool) 0);  // bool(false)
    var_dump((bool) 10234);  // bool(true)

    $var = 10;
    $var2 = "Abdullah";
    $var3 = false;
    $var4 = array("aboud", 10, "2005/10/10");
    echo gettype($var);
    echo "  //gettype<br/>";
    echo var_dump($var);
    echo "  //var_dump<br/>";
    echo gettype($var2);
    echo "  //gettype<br/>";
    echo var_dump($var2);
    echo "  //var_dump<br/>";
    echo gettype($var3);
    echo "  //gettype<br/>";
    echo var_dump($var3);
    echo "  //var_dump<br/>";
    echo gettype($var4);
    echo "  //gettype <br/>";
    echo var_dump($var4);
    echo "  //var_dump";


    // How to use functins array() with foreach functions
    $info = array("name" => "aboud", "age" => "20");
    echo $info['age'];
    echo $info['name'];
    echo "<br/> <br/>";

    $text = array("aboud", "ali", "omer");
    foreach($text as $key) {
        echo $key . "<br/>";
    }

    $arr = array(
        "color" => "white",
        "background-color" => "black",
        "font-size" => "10px"
    );
    foreach($arr as $keys => $value) {
        echo $keys . " : " . $value . "<br/>"; 
    }
    
    //  كيفيه الكتابه على عده سطور
    echo 'Hi \'PHP\'';
    ECHO '<br/>';
    echo "Hi \PHP\\";
    echo "<br/>";
    echo "Hi PHP 
        and Hi python";
    echo "<br/>";   

    //  nl2br()   وظيفتها هي مسح كل السطر و دمج الكلام في سطر واحد ولو كان في عده اسطر
    echo nl2br("Hi PHP
    and Hi python
    and Hi JavaScript");
    echo "<br/>";
    echo "Hi PHP and Hi python";

    $name = "Abdullah";

    // Heredoc      //   انها تفهم اي كلمه محجوزه او تتعامل معها على ان اي شي يمكن فهمه برمجيا يمكن استقبال المتغيرات و التخطي
    echo <<<"Here"
    Hi $name What are you doing now? : \\ watch or \\ clean .
    HI $name How are you 

    Here;


    // Nowdoc    الفرق هنا انه اي شيء تكتبه لو كانت كلمات محجوزه في الرنامج لن يتم تفسيرها او التعامل معها على انها كود برمجي بل بالكامل انها string.
    echo <<<'Now'
    Hi $name How are you \\
    Hi $name What are you doing now? : \\ watch or \\ clean .
    if $name is not "abdullah"
    Now;
    
    // Learn How to find defrent use between type variables (global variables) and (static variables) and (local variables).
    $global = 18;
    function add() {
        echo "My old $GLOBALS[global]";
        echo "<br/>";
    };

    function add1() {
        global $global;
        echo "My old $global";
        echo "<br/>";
    };
    
    function add2() {
        static $count = 0;
        $count++;
        echo $count . "<br/>";
    }
    function add3() {
        $GLOBALS['global'] = 20;
    }
    add3();
    echo $global;   // 20

    add();
    add1();
    add2(); // 1
    add2(); // 2
    add2(); // 3

    // Used Global Variables
    $name = "aboud";
    function add5() {
        global $name;
        $name = "Abdullah";
    }
    add();
    echo $name;

    // defrent print and echo
    $result = print "Hello";
    if ($result) {
        echo("OK");
    }else {
        echo("No");
    }

    // strlen and str_word_count
    $strlen = "Abdullah";
    $NumWord = "A b d";
    echo strlen($strlen);  //  تحصب عدد الحروف و مع المسافات و كل شيء تعظيك طزل السلسلة
    echo "<br/>";
    echo str_word_count($NumWord);    //  تحصب عدد الكلامات اي كم كلمه موجوده في النص المتغير 

    // strpos()
    $strpos = "Hello World!";
    echo strpos($strpos, "!");   // تبحث عن نص داخل متغير او داخل سلسله نصيه و تعطيك ال index تبعها بدايه ال index 

    $strtoupper = "hello world!";
    $strtolower = "HELLO WORLD!";
    $strreplace = "Hello World!";
    echo strtoupper($strtoupper);    // يكبر الأحرف
    echo "<br>";
    echo strtolower($strtolower);   //  تصغير الأحرف
    echo "<br>";
    echo strcasecmp($strtolower, $strtoupper);   //  مقارنه بين متغيرين  او بين نصين لكن لا تراعي حاله الاحرف كبيره او صغيره
    echo "<br/>";
    echo strcmp($strtolower, $strtoupper);    // مقاره حساسة لي حاله الأحرف تقارن بالضبط ما تم رصده من اختلاف 
    echo "<br/>";
    echo str_replace("Hello", "Hi", $strreplace);   //  تستبد مكان كلمه في نص الى كلمه ان تضعها هي تبحث عن الكلمه المراد استبدالها في المتغير تجدها تستبدلها في المعطى اليها 
    echo "<br/>";
    echo strrev($strreplace);    // يعكس الكلمه
    echo "<br/>";
    echo trim($strreplace);     //  تزيل المسافات التي في البداية و النهاية  
    echo "<br/>";
    $exp = explode(" ", $strreplace);  //  هذه تستخدم لي تقسيم الكلمه التي داخل النص الى مصفوفه او array  
    print_r($exp);   //  تستخدم ال print_r مع ال explode  // Array ( [0] => Hello [1] => World )
    echo "<br/>";
    
    $x = "Hello, World!";
    echo substr($x, 6, 6);  // هذه ارجاع قيمه بي استخدام ال index الرقم الذي تحدده في الاول هو مكان البدايه علما ان مكان البدايه محسوبه في ال length و الرقم الثاني هو ال length اي عددالكلمه الذي بدأت منه نحسب ال index.
    // \'	   Single Quote	
    // \"	   Double Quote	
    // \$	   PHP variables	
    // \n	   New Line	
    // \r	   Carriage Return	
    // \t	   Tab	
    // \f	   Form Feed	
    // \ooo	   Octal value	
    // \xhh	   Hex value

    $object = "Hello";
    $object = (object) $object;
    echo var_dump($object);  // Data Type: object(stdClass#1) { ["scalar"]=> string(5) "Hello" }
    echo "<br/>";
    echo gettype($object);   // Data Type: (object)

    $xx = "HI";
    $xx = (unset) $xx;
    echo var_dump($xx);  // هذا سيكون فارغا انتهيت التعيين عليه

    $is_name = "david";
    $exp1 = 10;
    $exp2 = 2.5 * 4;
    $is_arr = [10, "20", "30", 30];
    echo var_dump($exp1);   // هنا نوع البيانات (integer) لانه عدد صحيح خالي من الفواصل والنقط
    echo "<br/>";
    echo var_dump($exp2);  // علما ان الجواب هو 10 لكن هذا المتغير ليس عدد صحيح انما هو عشري نوع البيانات هو (float) هو لا يأخذ الخواب اما لي احتواءه قيمه عشريه 
    echo "<br/>";

    echo is_int($exp1) || is_integer($exp1) || is_long($exp1);  //  لي الـأكد من انه عدد صحيح سوف يعطيك 1 اذا كان صحيح لن يعطيك شي اذا لم يكن صحيح 
    echo "<br/>";
    echo is_float($exp2);    //  لي التأكد من انه عدد  عشري يعطي 1 اذا لم يكن لا يعطي شيء
    echo "<br/>";
    echo is_double($exp1);
    echo "<br/>";
    echo is_string($is_name);
    echo "<br/>";
    echo is_array($is_arr);
