.source BKoolClass.java
.class public BKoolClass
.super java.lang.Object

.method public static <clinit>()V
Label0:
Label1:
	return
.limit stack 0
.limit locals 0
.end method

.method public <init>(I)V
.var 0 is this LBKoolClass; from Label0 to Label1
.var 1 is b I from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a LBKoolClass; from Label0 to Label1
	new BKoolClass
	dup
	bipush 100
	invokespecial BKoolClass/<init>(I)V
	astore_1
	aload_1
	invokevirtual BKoolClass/printD()V
	iconst_1
	invokestatic io/writeInt(I)V
Label1:
	return
.limit stack 3
.limit locals 2
.end method

.method public printD()V
Label0:
.var 0 is this LBKoolClass; from Label0 to Label1
	ldc "D"
	invokestatic io/writeStr(Ljava/lang/String;)V
Label1:
	return
.limit stack 1
.limit locals 1
.end method
