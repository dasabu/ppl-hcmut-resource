.source BKoolClass.java
.class public BKoolClass
.super java.lang.Object
.field fname Ljava/lang/String;
.field lname Ljava/lang/String;
.field age I

.method public <init>()V
.var 0 is this LBKoolClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	ldc "John"
	putfield BKoolClass/fname Ljava/lang/String;
	aload_0
	ldc "Doe"
	putfield BKoolClass/lname Ljava/lang/String;
	aload_0
	bipush 24
	putfield BKoolClass/age I
Label1:
	return
.limit stack 2
.limit locals 1
.end method

.method public static <clinit>()V
Label0:
Label1:
	return
.limit stack 0
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is myObj LBKoolClass; from Label0 to Label1
	new BKoolClass
	dup
	invokespecial BKoolClass/<init>()V
	astore_1
	aload_1
	getfield BKoolClass/fname Ljava/lang/String;
	aload_1
	getfield BKoolClass/lname Ljava/lang/String;
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	invokestatic io/writeStr(Ljava/lang/String;)V
	aload_1
	getfield BKoolClass/age I
	invokestatic io/writeInt(I)V
Label1:
	return
.limit stack 2
.limit locals 2
.end method
