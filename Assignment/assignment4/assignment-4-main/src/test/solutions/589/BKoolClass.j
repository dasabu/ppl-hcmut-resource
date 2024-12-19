.source BKoolClass.java
.class public BKoolClass
.super java.lang.Object
.field total [I

.method public <init>()V
.var 0 is this LBKoolClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	iconst_4
	newarray int
	dup
	iconst_0
	iconst_0
	iastore
	dup
	iconst_1
	iconst_0
	iastore
	dup
	iconst_2
	iconst_0
	iastore
	dup
	iconst_3
	iconst_0
	iastore
	putfield BKoolClass/total [I
Label1:
	return
.limit stack 5
.limit locals 1
.end method

.method public static <clinit>()V
Label0:
Label1:
	return
.limit stack 0
.limit locals 0
.end method

.method public change(I)V
Label0:
.var 0 is this LBKoolClass; from Label0 to Label1
.var 1 is i I from Label0 to Label1
	aload_0
	getfield BKoolClass/total [I
	iload_1
	bipush 100
	iastore
Label1:
	return
.limit stack 7
.limit locals 2
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
	iconst_0
	istore_2
Label2:
	iload_2
	iconst_3
	if_icmpgt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
Label6:
	aload_1
	getfield BKoolClass/total [I
	iload_2
	iaload
	invokestatic io/writeInt(I)V
Label7:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label2
Label3:
Label1:
	return
.limit stack 6
.limit locals 3
.end method
