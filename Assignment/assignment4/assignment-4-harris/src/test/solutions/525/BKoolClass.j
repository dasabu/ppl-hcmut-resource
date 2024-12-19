.source BKoolClass.java
.class public BKoolClass
.super java.lang.Object

.method public <init>()V
.var 0 is this LBKoolClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
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
.var 1 is sum1 I from Label0 to Label1
	bipush 100
	bipush 50
	iadd
	istore_1
.var 2 is sum2 I from Label0 to Label1
	iload_1
	sipush 250
	iadd
	istore_2
.var 3 is sum3 I from Label0 to Label1
	iload_2
	iload_2
	iadd
	istore_3
	iload_3
	invokestatic io/writeInt(I)V
Label1:
	return
.limit stack 2
.limit locals 4
.end method
