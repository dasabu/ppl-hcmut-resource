.source BKoolClass.java
.class public BKoolClass
.super java.lang.Object
.field static d F
.field bb F

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
.var 1 is d F from Label0 to Label1
.var 2 is e Z from Label0 to Label1
	iconst_1
	iconst_0
	if_icmpge Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	bipush 7
	bipush 8
	if_icmple Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ior
	istore_2
	iload_2
	invokestatic io/writeBool(Z)V
Label1:
	return
.limit stack 8
.limit locals 3
.end method
