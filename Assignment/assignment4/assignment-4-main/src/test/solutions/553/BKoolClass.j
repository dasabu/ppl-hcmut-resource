.source BKoolClass.java
.class public BKoolClass
.super java.lang.Object
.field a I

.method public <init>()V
.var 0 is this LBKoolClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	bipush 10
	putfield BKoolClass/a I
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

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is bk LBKoolClass; from Label0 to Label1
	new BKoolClass
	dup
	invokespecial BKoolClass/<init>()V
	astore_1
	iconst_1
	bipush 17
	if_icmpge Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
Label5:
	aload_1
	getfield BKoolClass/a I
	invokestatic io/writeInt(I)V
Label6:
Label4:
Label1:
	return
.limit stack 3
.limit locals 2
.end method
