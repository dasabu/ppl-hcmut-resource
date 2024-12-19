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
	iconst_1
	invokestatic BKoolClass/isEqual(II)Z
	invokestatic io/writeBool(Z)V
Label1:
	return
.limit stack 2
.limit locals 1
.end method

.method public static isEqual(II)Z
Label0:
.var 0 is a I from Label0 to Label1
.var 1 is b I from Label0 to Label1
	iconst_1
	iload_1
	if_icmple Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	iconst_1
	ireturn
Label4:
	iconst_0
	ireturn
Label5:
Label1:
.limit stack 5
.limit locals 2
.end method
