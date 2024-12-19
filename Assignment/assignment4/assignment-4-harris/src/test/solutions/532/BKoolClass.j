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
.var 1 is i I from Label0 to Label1
	iconst_0
	istore_1
Label2:
	iload_1
	bipush 9
	if_icmpgt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
Label6:
.var 2 is y I from Label6 to Label7
	iload_1
	iconst_4
	if_icmpne Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label10
	goto Label3
Label10:
	iload_1
	invokestatic io/writeInt(I)V
Label7:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label2
Label3:
Label1:
	return
.limit stack 8
.limit locals 3
.end method
