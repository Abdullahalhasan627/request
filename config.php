<?php
// إعداد بيانات الاتصال
$host = 'localhost'; // اسم الخادم
$dbname = 'aboud'; // اسم قاعدة البيانات
$username = 'root';  // اسم المستخدم
$password = '500201'; // كلمة المرور

try {
    // إنشاء اتصال PDO
    $dsn = "mysql:host=$host;dbname=$dbname;charset=utf8mb4"; // DSN للاتصال
    $pdo = new PDO($dsn, $username, $password);

    // تعيين إعدادات PDO
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION); // تفعيل الأخطاء
    $pdo->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_ASSOC); // نوع النتائج

    echo "تم الاتصال بقاعدة البيانات بنجاح!";
} catch (PDOException $e) {
    // معالجة الأخطاء
    die("فشل الاتصال بقاعدة البيانات: " . $e->getMessage());
}
?>
