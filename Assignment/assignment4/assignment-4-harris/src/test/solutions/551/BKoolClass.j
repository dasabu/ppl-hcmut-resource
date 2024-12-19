.source BKoolClass.java
.class public BKoolClass
.super java.lang.Object
.field x I

.method public <init>()V
.var 0 is this LBKoolClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	iconst_5
	putfield BKoolClass/x I
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
.var 1 is myObj1 LBkoolClass; from Label0 to Label1
	new BKoolClass
	dup
	invokespecial BKoolClass/<init>()V
	astore_1
.var 2 is myObj2 LBkoolClass; from Label0 to Label1
	new BKoolClass
	dup
	invokespecial BKoolClass/<init>()V
	astore_2
.var 3 is a I from Label0 to Label1
	bipush 100
	istore_3
	aload_2
	bipush 25
	putfield BKoolClass/x I
	aload_2
	getfield BKoolClass/x I
	aload_1
	getfield BKoolClass/x I
	iadd
	iload_3
	iadd
	invokestatic io/writeInt(I)V
Label1:
	return
.limit stack 5
.limit locals 4
.end method
