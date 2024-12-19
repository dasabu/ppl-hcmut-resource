.source BKoolClass.java
.class public BKoolClass
.super java.lang.Object
.field z I

.method public <init>()V
.var 0 is this LBKoolClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	bipush 6
	putfield BKoolClass/z I
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
.var 0 is this LBKoolClass; from Label0 to Label1
	aload_0
	getfield BKoolClass/z I
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
	aload_1
	invokevirtual BKoolClass/foo()V
Label1:
	return
.limit stack 2
.limit locals 2
.end method
