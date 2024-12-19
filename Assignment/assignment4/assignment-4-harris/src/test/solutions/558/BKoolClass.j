.source BKoolClass.java
.class public BKoolClass
.super java.lang.Object
.field a I
.field b I

.method public <init>()V
.var 0 is this LBKoolClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	bipush 10
	putfield BKoolClass/a I
	aload_0
	bipush 20
	putfield BKoolClass/b I
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

.method public foo(I)I
Label0:
.var 0 is this LBKoolClass; from Label0 to Label1
.var 1 is x I from Label0 to Label1
	iload_1
	ireturn
Label1:
.limit stack 1
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
	aload_1
	getfield BKoolClass/a I
	aload_1
	getfield BKoolClass/b I
	if_icmpge Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	aload_1
	aload_1
	getfield BKoolClass/b I
	putfield BKoolClass/a I
Label4:
	aload_1
	getfield BKoolClass/a I
	invokestatic io/writeInt(I)V
Label1:
	return
.limit stack 7
.limit locals 2
.end method
