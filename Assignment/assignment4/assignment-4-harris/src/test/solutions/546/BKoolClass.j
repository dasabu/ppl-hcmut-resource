.source BKoolClass.java
.class public BKoolClass
.super java.lang.Object
.field x I

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
.var 1 is myObj LBKoolClass; from Label0 to Label1
	new BKoolClass
	dup
	invokespecial BKoolClass/<init>()V
	astore_1
	aload_1
	bipush 25
	putfield BKoolClass/x I
	aload_1
	getfield BKoolClass/x I
	invokestatic io/writeInt(I)V
Label1:
	return
.limit stack 5
.limit locals 2
.end method
