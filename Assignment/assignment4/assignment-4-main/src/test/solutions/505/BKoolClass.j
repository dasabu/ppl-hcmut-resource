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
	iconst_1
	invokestatic io/writeInt(I)V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static add(II)I
Label0:
.var 0 is a I from Label0 to Label1
.var 1 is b I from Label0 to Label1
	iload_0
	iload_1
	iadd
	ireturn
Label1:
.limit stack 2
.limit locals 2
.end method
