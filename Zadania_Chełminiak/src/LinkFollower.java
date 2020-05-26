import javax.swing.event.HyperlinkEvent;
import javax.swing.event.HyperlinkListener;
import java.awt.*;
import java.net.URI;
import java.net.URISyntaxException;
import java.net.URL;

public class LinkFollower implements HyperlinkListener {


    public void hyperlinkUpdate(HyperlinkEvent evt) {
        //Create hyperlink listener, which opens browser when hyperlink is clicked in JEditorPane
        if (evt.getEventType() == HyperlinkEvent.EventType.ACTIVATED) {
            try {
                openWebpage(evt.getURL());
            } catch (Exception e) {
            }
        }
    }

    public static boolean openWebpage(URI uri) {
        //Use desktop class to run application from native desktop
        Desktop desktop = Desktop.isDesktopSupported() ? Desktop.getDesktop() : null;
        if (desktop != null && desktop.isSupported(Desktop.Action.BROWSE)) {
            try {
                //Launch default browser and handle and URI to it
                desktop.browse(uri);
                return true;
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
        return false;
    }

    public static boolean openWebpage(URL url) {
        //Convert URL (Uniform Resource Locator) address to URI (Uniform Resource Identifier)
        try {
            return openWebpage(url.toURI());
        } catch (URISyntaxException e) {
            e.printStackTrace();
        }
        return false;
    }

}
