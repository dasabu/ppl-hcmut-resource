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

.method public foo()V
Label0:
.var 0 is this LBKoolClass; from Label0 to Label1
	iconst_1
	invokestatic io/writeInt(I)V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is bk LBKoolClass; from Label0 to Label1
	new BKoolClass
	dup
	invokespecial BKoolClass/<init>()V
	astore_1
.var 2 is i I from Label0 to Label1
	iconst_0
	istore_2
	iconst_1
	istore_2
Label2:
	iload_2
	iconst_5
	if_icmpgt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
	aload_1
	invokevirtual BKoolClass/foo()V
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label2
Label3:
Label1:
	return
.limit stack 7
.limit locals 3
.end method
