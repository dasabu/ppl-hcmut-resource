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

.method public static myStaticMethod()V
Label0:
	ldc "Static methods can be called without creating objects"
	invokestatic io/writeStrLn(Ljava/lang/String;)V
Label1:
	return
.limit stack 1
.limit locals 0
.end method

.method public myPublicMethod()V
Label0:
.var 0 is this LBKoolClass; from Label0 to Label1
	ldc "Public methods must be called by creating objects"
	invokestatic io/writeStr(Ljava/lang/String;)V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is myObj LBKoolClass; from Label0 to Label1
	new BKoolClass
	dup
	invokespecial BKoolClass/<init>()V
	astore_1
	invokestatic BKoolClass/myStaticMethod()V
	aload_1
	invokevirtual BKoolClass/myPublicMethod()V
Label1:
	return
.limit stack 2
.limit locals 2
.end method
