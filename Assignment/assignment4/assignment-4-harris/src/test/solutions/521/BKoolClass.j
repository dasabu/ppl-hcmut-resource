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
.var 1 is a Ljava/lang/String; from Label0 to Label1
	ldc "a"
	astore_1
.var 2 is b Ljava/lang/String; from Label0 to Label1
	ldc "b"
	astore_2
	ldc "abc"
	aload_2
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	invokestatic io/writeStr(Ljava/lang/String;)V
Label1:
	return
.limit stack 2
.limit locals 3
.end method
