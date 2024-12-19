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
.var 1 is result I from Label0 to Label1
	bipush 10
	invokestatic BKoolClass/sum(I)I
	istore_1
	iload_1
	invokestatic io/writeInt(I)V
Label1:
	return
.limit stack 1
.limit locals 2
.end method

.method public static sum(I)I
Label0:
.var 0 is k I from Label0 to Label1
	iload_0
	iconst_0
	if_icmple Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
Label5:
	iload_0
	iload_0
	iconst_1
	isub
	invokestatic BKoolClass/sum(I)I
	iadd
	ireturn
Label6:
Label4:
Label8:
	iconst_0
	ireturn
Label9:
Label7:
Label1:
.limit stack 5
.limit locals 1
.end method
