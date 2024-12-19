.source Main.java
.class public Main
.super java.lang.Object

.method public <init>()V
.var 0 is this LMain; from Label0 to Label1
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

.method public fullThrottle()V
Label0:
.var 0 is this LMain; from Label0 to Label1
	ldc "The car is going as fast as it can!"
	invokestatic io/writeStrLn(Ljava/lang/String;)V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public speed(Ljava/lang/String;)V
Label0:
.var 0 is this LMain; from Label0 to Label1
.var 1 is maxSpeed Ljava/lang/String; from Label0 to Label1
	ldc "Max speed is: "
	aload_1
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	invokestatic io/writeStrLn(Ljava/lang/String;)V
Label1:
	return
.limit stack 2
.limit locals 2
.end method
