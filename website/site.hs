{-# LANGUAGE OverloadedStrings #-}
import Data.List (isSuffixOf)
import Data.Monoid ((<>))
import Data.Time (defaultTimeLocale, formatTime, getCurrentTime, UTCTime)
import System.FilePath.Posix (takeBaseName,takeFileName,(</>))
import Hakyll


timeFormat :: String
timeFormat = "1%Y-%m-%d at %H:%M UTC"
-------------------------------------------------------------------------------
main :: IO ()
main = hakyll . hakyllRules =<< getCurrentTime

hakyllRules :: UTCTime -> Rules ()
hakyllRules gentime = do
    let genTimeCtx = constField "gentime" timestring <> defaultContext where 
            timestring = formatTime defaultTimeLocale timeFormat gentime
    let mainCtx = context genTimeCtx

    match "templates/*" $
        compile templateBodyCompiler

    match "images/*" $ 
        route idRoute >> compile copyFileCompiler

    match "css/*" $ 
        route idRoute >> compile compressCssCompiler

    match "main/robots.txt" $ 
        route topRoute >> compile copyFileCompiler

    match ("main/*.md") $ do
        route $ customRoute ((</> "index.html") . takeBaseName . toFilePath)
        compile $ pandocCompiler
--             >>= theUsual genTimeCtx
            >>= theUsual mainCtx

    match "main/index.html" $ do
        route topRoute
        compile $ do
            getResourceBody
--                 >>= applyAsTemplate genTimeCtx
--                 >>= theUsual genTimeCtx
                >>= applyAsTemplate mainCtx
                >>= theUsual mainCtx

-------------------------------------------------------------------------------
-- routes
topRoute :: Routes
topRoute = customRoute (takeFileName . toFilePath)

-------------------------------------------------------------------------------
-- compilers
theUsual :: Context String -> Item String -> Compiler (Item String)
theUsual ctx item = loadAndApplyTemplate "templates/default.html" ctx item
    >>= relativizeUrls
    >>= cleanIndexUrls

-- removes index.html from the ends of links
cleanIndexUrls :: Item String -> Compiler (Item String)
cleanIndexUrls = return . fmap (withUrls cleanIndex) where
    cleanIndex :: String -> String
    cleanIndex url
        | idx `isSuffixOf` url = take (length url - length idx) url
        | otherwise            = url
      where idx = "index.html"

context :: Context a -> Context a
context ctx = constField "name" "arrondissement"
        <> constField "area" "100km^2"
        <> constField "population" "wow lots"
        <> constField "density" "so dense"
        <> ctx
