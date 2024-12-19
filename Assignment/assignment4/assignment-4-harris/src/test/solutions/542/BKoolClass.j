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
	bipush 20
	invokestatic BKoolClass/checkAge(I)V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static checkAge(I)V
Label0:
.var 0 is age I from Label0 to Label1
	iload_0
	bipush 18
	if_icmpge Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	ldc "Access denied - You are not old enough!"
	invokestatic io/writeStr(Ljava/lang/String;)V
	goto Label5
Label4:
	ldc "Access granted - You are old enough!"
	invokestatic io/writeStr(Ljava/lang/String;)V
Label5:
Label1:
	return
.limit stack 3
.limit locals 1
.end method
