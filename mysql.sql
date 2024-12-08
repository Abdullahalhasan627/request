CREATE USER 'aboud'@'localhost' IDENTIFIED BY '500201';

GRANT ALL PRIVILEGES ON *.* TO 'aboud'@'localhost'; 
GRANT PRIVILEGES ON aboud.* TO 'aboud'@'localhost';
GRANT SELECT ON aboud.* TO 'aboud'@'localhost';
GRANT CREATE ON aboud.* TO 'aboud'@'localhost';
GRANT DROP ON aboud.* TO aboud;

REVOKE SELECT ON *.* FROM 'aboud'@'localhost';
REVOKE DROP ON aboud.* FROM 'aboud'@'localhost';
REVOKE CREATE ON aboud.* FROM 'aboud'@'localhost';
REVOKE INSERT ON aboud.* FROM 'aboud'@'localhost';
REVOKE UPDATE ON aboud.* FROM 'aboud'@'localhost';
REVOKE ALL PRIVILEGES ON aboud.* FROM 'aboud'@'localhost';
REVOKE PRIVILEGES ON aboud.* FROM 'aboud'@'localhost';

REVOKE USER 'aboud'@'localhost' TO 'abdullah'@'localhost';

ALTER USER 'abdullah'@'localhost' IDENTIFIED BY '101011';

FLUSH PRIVILEGES;    // لي حفظ تغيرات التعديل على الحساب  من حذف وانشاء و تعديل وصلاحيات 

CREATE TABLE aboud.pet (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT DEFAULT - , age INT NOT NULL, name VARCHAR(255) NOT NULL)    


في SQL، هناك قسمان رئيسيان يجب التفريق بينهما:

أنواع البيانات (Data Types): تحدد نوع البيانات التي يمكن تخزينها في الأعمدة.
القيود (Constraints): تُستخدم لتحديد قواعد حول القيم المخزنة في الأعمدة.
أولًا: أنواع البيانات (Data Types)
1. الأنواع العددية (Numeric Data Types):
النوع	الوصف
INT	عدد صحيح.
SMALLINT	عدد صحيح صغير.
BIGINT	عدد صحيح كبير.
DECIMAL(p,s)	أرقام عشرية بدقة محددة. (p: عدد الأرقام الكلية، s: عدد الأرقام بعد الفاصلة)
FLOAT	أرقام عشرية عائمة.
DOUBLE	أرقام عشرية ذات دقة مزدوجة.
TINYINT	أعداد صغيرة جدًا (غالبًا تُستخدم للأعلام مثل 0 و 1).
2. النصوص (Character/String Data Types):
النوع	الوصف
CHAR(n)	سلسلة نصية بطول ثابت (n).
VARCHAR(n)	سلسلة نصية بطول متغير (حتى n).
TEXT	نص طويل.
TINYTEXT	نص قصير جدًا.
MEDIUMTEXT	نص متوسط الطول.
LONGTEXT	نص طويل جدًا.
3. التواريخ والأوقات (Date and Time Data Types):
النوع	الوصف
DATE	تاريخ (YYYY-MM-DD).
DATETIME	تاريخ ووقت (YYYY-MM-DD HH:MM:SS).
TIMESTAMP	تاريخ ووقت مع المنطقة الزمنية.
TIME	وقت فقط (HH:MM:SS).
YEAR	سنة فقط (YYYY).
4. الأنواع الثنائية (Binary Data Types):
النوع	الوصف
BLOB	بيانات ثنائية (Binary Large Object).
TINYBLOB	بيانات ثنائية صغيرة جدًا.
MEDIUMBLOB	بيانات ثنائية متوسطة الحجم.
LONGBLOB	بيانات ثنائية كبيرة جدًا.
ثانيًا: القيود (Constraints)
1. PRIMARY KEY:
يُستخدم لتحديد عمود (أو مجموعة أعمدة) كمفتاح أساسي.
يضمن أن القيم فريدة وغير فارغة.
2. FOREIGN KEY:
يُستخدم لربط عمود بمفتاح أساسي في جدول آخر.
3. NOT NULL:
يمنع العمود من قبول القيم الفارغة.
4. UNIQUE:
يضمن أن القيم في العمود فريدة.
5. DEFAULT:
يحدد قيمة افتراضية للعمود.
6. CHECK:
يفرض شرطًا على القيم المدخلة.
7. AUTO_INCREMENT:
يُستخدم لتحديد عمود رقمي يزيد تلقائيًا.
8. ON DELETE CASCADE:
يُحدد ما يحدث إذا تم حذف صف مرتبط.
9. UNSIGNED:
يُستخدم مع الأعمدة العددية ويمنع القيم السالبة.

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,       -- معرف المستخدم مفتاح أساسي
    name VARCHAR(100) NOT NULL,              -- الاسم، غير فارغ
    age INT CHECK (age >= 18),               -- العمر، شرط أن يكون 18 أو أكثر
    email VARCHAR(100) UNIQUE,               -- البريد الإلكتروني فريد
    balance DECIMAL(10, 2) DEFAULT 0.00      -- الرصيد، القيمة الافتراضية 0
);

ChatGPT
في SQL، الأنواع التي يتم كتابتها بجانب الأعمدة مثل PRIMARY KEY تُعرف بـ القيود (Constraints). هذه القيود تحدد كيفية التعامل مع البيانات داخل الأعمدة وتضع قواعد لضمان صحة البيانات واتساقها.

فيما يلي قائمة بأنواع القيود مع شرح لكل منها وأمثلة:

أنواع القيود (Constraints):
PRIMARY KEY:

يُستخدم لتحديد عمود (أو مجموعة أعمدة) يُعتبر المفتاح الأساسي للجدول.
المفتاح الأساسي يضمن أن كل قيمة داخل العمود فريدة وغير فارغة (NOT NULL).
كل جدول يمكن أن يحتوي على مفتاح أساسي واحد فقط.
مثال:

sql
نسخ الكود
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(50)
);
FOREIGN KEY:

يُستخدم لتحديد عمود يكون مفتاحًا خارجيًا مرتبطًا بمفتاح أساسي في جدول آخر.
يضمن التكامل المرجعي بين الجدولين.
مثال:

sql
نسخ الكود
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);
NOT NULL:

يمنع العمود من قبول القيم الفارغة (NULL).
مثال:

sql
نسخ الكود
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);
UNIQUE:

يضمن أن جميع القيم في العمود فريدة.
مثال:

sql
نسخ الكود
CREATE TABLE users (
    user_id INT PRIMARY KEY,
    email VARCHAR(100) UNIQUE
);
DEFAULT:

يُحدد قيمة افتراضية للعمود في حال لم يتم إدخال قيمة.
مثال:

sql
نسخ الكود
CREATE TABLE accounts (
    account_id INT PRIMARY KEY,
    balance DECIMAL(10, 2) DEFAULT 0.00
);
CHECK:

يُستخدم لفرض شرط معين على القيم المدخلة في العمود.
مثال:

sql
نسخ الكود
CREATE TABLE employees (
    id INT PRIMARY KEY,
    age INT CHECK (age >= 18)
);
AUTO_INCREMENT:

يُستخدم مع الأعمدة الرقمية لزيادة قيمتها تلقائيًا عند إدخال صف جديد.
مثال:

sql
نسخ الكود
CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    order_date DATE
);
INDEX:

يُستخدم لتحسين سرعة استرجاع البيانات من الجداول.
مثال:

sql
نسخ الكود
CREATE INDEX idx_name ON employees(name);
ON DELETE CASCADE و ON UPDATE CASCADE:

تُستخدم مع المفاتيح الخارجية لتحديد ما يحدث عند حذف أو تحديث البيانات المرتبطة.
مثال:

sql
نسخ الكود
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    FOREIGN KEY (customer_id) REFERENCES customers(id) ON DELETE CASCADE
);
UNSIGNED:

خاص بالأعمدة الرقمية ويضمن أن القيم المدخلة غير سالبة.
مثال:

sql
نسخ الكود
CREATE TABLE accounts (
    account_id INT PRIMARY KEY,
    balance INT UNSIGNED
);


-- LOAD DATA LOCAL INFILE 'C:\\Users\\Mohammed\\OneDrive\\Desktop\\Code\\info.csv'
-- INTO TABLE pet_up
-- FIELDS TERMINATED BY ','+-
-- LINES TERMINATED BY '\n'
-- IGNOROWS
-- (id, age, name);

-- CREATE USER 'aboud'@'localhost' IDENTIFIED BY '500201'
DESCRIBE