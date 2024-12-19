.source a.java
.class public a
.super java.lang.Object

.method public <init>()V
.var 0 is this La; from Label0 to Label1
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
.var 1 is dem I from Label0 to Label1
	invokestatic b/foo2()I
	istore_1
	iload_1
	invokestatic io/writeFloat(F)V
Label1:
	return
.limit stack 3
.limit locals 2
.end method
