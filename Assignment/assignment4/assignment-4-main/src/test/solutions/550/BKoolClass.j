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
.var 1 is myCar LMain; from Label0 to Label1
	new Main
	dup
	invokespecial Main/<init>()V
	astore_1
	aload_1
	invokevirtual Main/fullThrottle()V
	aload_1
	ldc "200"
	invokevirtual Main/speed(Ljava/lang/String;)V
Label1:
	return
.limit stack 3
.limit locals 2
.end method
