.source MP.java
.class public MP
.super java.lang.Object
.field a I

.method public <init>()V
.var 0 is this LMP; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	bipush 11
	putfield MP/a I
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

.method public foo()V
Label0:
.var 0 is this LMP; from Label0 to Label1
	bipush 11
	invokestatic io/writeInt(I)V
Label1:
	return
.limit stack 1
.limit locals 1
.end method
