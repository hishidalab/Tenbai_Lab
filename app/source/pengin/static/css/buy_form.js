$(document).ready(function() {
  $(".sub-img").click(function() {
    var mainImgSrc = $(this).attr("src");
    var mainImgAlt = $(this).attr("alt");
    $(".main-img").attr("src", mainImgSrc);
    $(".main-img").attr("alt", mainImgAlt);
    $(".main-img").removeClass("rounded-pill"); // rounded-pill クラスを削除
    $(".main-img").addClass("enlarged-img"); // enlarged-img クラスを追加
  });
});
